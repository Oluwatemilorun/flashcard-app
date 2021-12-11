<template>
	<v-container fill-height>
		<div class="top-bar py-5">
			<v-row no-gutters justify="center" align="center">
				<v-btn outlined to="/backdoor/cards">
					<v-icon left>mdi-cog</v-icon>
					Manage cards
				</v-btn>
			</v-row>
		</div>

		<v-row no-gutters justify="center" align="center" class="fill-height">
			<v-progress-circular v-if="loadingCards" indeterminate size="48" />
			<v-col
				v-else-if="!loadingCards && cards.length >= 1"
				cols="10"
				md="8"
				lg="6"
				class="flashcard-wrapper"
			>
				<div
					v-for="(card, i) in cards"
					:key="i"
					:class="{
						'remove-right': card.status === 'correct',
						'remove-left': card.status === 'wrong',
					}"
					class="flashcard-stacker"
				>
					<flash-card
						:front="card.phrase"
						:back="card.definition"
						:flipped="showDefinition"
						focused
						class="mx-auto"
					></flash-card>
				</div>
			</v-col>
			<v-col v-else cols="10" md="8" lg="6" class="flashcard-wrapper">
				<div class="h5 font-weight-light text-center">{{ status }}</div>
			</v-col>
		</v-row>

		<div class="controls-wrapper py-5">
			<v-row no-gutters justify="center" align="center">
				<v-col cols="10" md="8" lg="6">
					<v-row v-if="showDefinition">
						<v-col class="flex-shrink-1">
							<v-btn outlined block :disabled="cards.length === 0" @click="next(false)">
								I did not get it
							</v-btn>
						</v-col>
						<v-col class="flex-shrink-1">
							<v-btn outlined block :disabled="cards.length === 0" @click="next(true)">
								I got it
							</v-btn>
						</v-col>
					</v-row>
					<v-row v-else>
						<v-col class="flex-shrink-1">
							<v-btn
								outlined
								block
								:disabled="cards.length === 0"
								@click="showDefinition = !showDefinition"
							>
								Show definition
							</v-btn>
						</v-col>
					</v-row>
				</v-col>
			</v-row>
		</div>

		<v-snackbar v-model="snackbar" :timeout="3000">
			{{ snackbarText }}

			<template #action="{ attrs }">
				<v-btn color="accent" text v-bind="attrs" @click="snackbar = false"> Close </v-btn>
			</template>
		</v-snackbar>
	</v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import { Flashcard } from '~/types/interfaces'

export default Vue.extend({
	data() {
		return {
			loadingCards: false,
			showDefinition: false,
			snackbar: false,
			snackbarText: '',
			removeType: '',
			cards: [] as (Flashcard & { status?: 'correct' | 'wrong' })[],
			cachedCards: [] as (Flashcard & { status?: 'correct' | 'wrong' })[],
		}
	},
	computed: {
		status() {
			const cachedCards = this.cachedCards.length === 0
			const flashCards = this.cards.length === 0

			// TODO: return based on bin value 'you have no more words to review; you are permanently done!' || 'You are temporarily done; please come back later to review more words.'
			if (cachedCards && flashCards)
				return 'You have no more words to review; you are permanently done!'
			else if (flashCards && !cachedCards)
				return 'You are temporarily done; please come back later to review more words.'
			else return 'No Cards Available'
		},
	},
	mounted() {
		this.getCards()
	},
	methods: {
		next(correct: boolean) {
			this.showDefinition = false
			this.cards[this.cards.length - 1].status = correct ? 'correct' : 'wrong'
			setTimeout(() => {
				const card = this.cards.pop()
				if (card) {
					if (correct) this.markCorrect(card)
					else this.markIncorrect(card)
				}
			}, 700)
		},
		showSnackbar(message: string) {
			this.snackbarText = message
			this.snackbar = true
		},
		updateCards(card: Flashcard) {
			const interval = card.current_bin.interval
			const willShow = new Date(card.bin_updated_at).getTime() + interval
			const currentTime = new Date().getTime()

			if (willShow > currentTime) {
				console.log('card will be ready in', willShow - currentTime, card)
				setTimeout(() => {
					this.cards = [card, ...this.cards]
				}, willShow - currentTime)
			} else {
				this.cards = [card, ...this.cards]
			}
		},
		async markCorrect(card: Flashcard) {
			try {
				const { data } = await this.$axios.put(`/v1/cards/${card.id}/mark-correct`)
				this.updateCards(data.payload)
			} catch (error) {
				setTimeout(() => this.markCorrect(card), 5000)
			}
		},
		async markIncorrect(card: Flashcard) {
			try {
				const { data } = await this.$axios.put(`/v1/cards/${card.id}/mark-incorrect`)
				this.updateCards(data.payload)
			} catch (error) {
				setTimeout(() => this.markIncorrect(card), 5000)
			}
		},
		async getCards() {
			this.loadingCards = true
			try {
				const { data } = await this.$axios.get('/v1/cards/flash')
				const cards = data.payload as Flashcard[]

				for (let i = 0; i < cards.length; i++) {
					const card = cards[i]
					const interval = card.current_bin.interval
					const willShow = new Date(card.bin_updated_at).getTime() + interval
					const currentTime = new Date().getTime()

					if (willShow <= currentTime) {
						// console.log('card is ready', card)
						this.cards = [card, ...this.cards]
					} else {
						// console.log('card will be ready in', willShow - currentTime, card)
						setTimeout(() => {
							this.cards = [card, ...this.cards]
						}, willShow - currentTime)
					}
				}

				this.cachedCards = cards
			} catch (error) {
				this.showSnackbar(error.response ? error.response.message : error.message)
			} finally {
				this.loadingCards = false
			}
		},
	},
})
</script>

<style lang="sass">
.flashcard-wrapper
	position: relative
	display: contents

.flashcard-stacker
	position: absolute
	left: 20px
	right: 20px
	margin: 0 auto

	transition: all 100ms ease-in-out

.top-bar
	position: absolute
	left: 0
	right: 0
	top: 0

.controls-wrapper
	position: absolute
	left: 0
	right: 0
	bottom: 0

.remove-right
	-webkit-animation: fade-out-right 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both
	animation: fade-out-right 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both

.remove-left
	-webkit-animation: fade-out-left 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both
	animation: fade-out-left 0.7s cubic-bezier(0.250, 0.460, 0.450, 0.940) both

@-webkit-keyframes fade-out-right
	0%
	-webkit-transform: translateX(0)
	transform: translateX(0)
	opacity: 1

	100%
	-webkit-transform: translateX(50px)
	transform: translateX(50px)
	opacity: 0

@keyframes fade-out-right
	0%
		-webkit-transform: translateX(0)
		transform: translateX(0)
		opacity: 1

	100%
		-webkit-transform: translateX(50px)
		transform: translateX(50px)
		opacity: 0

@-webkit-keyframes fade-out-left
	0%
	-webkit-transform: translateX(0)
	transform: translateX(0)
	opacity: 1

	100%
	-webkit-transform: translateX(-50px)
	transform: translateX(-50px)
	opacity: 0

@keyframes fade-out-left
	0%
		-webkit-transform: translateX(0)
		transform: translateX(0)
		opacity: 1

	100%
		-webkit-transform: translateX(-50px)
		transform: translateX(-50px)
		opacity: 0
</style>
