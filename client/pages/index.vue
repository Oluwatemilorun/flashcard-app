<template>
	<v-container fill-height>
		<v-row no-gutters justify="center" align="center" class="fill-height">
			<v-col v-if="cards.length >= 1" cols="10" md="8" lg="6" class="flashcard-wrapper">
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
					<v-row>
						<v-col class="flex-shrink-1" order="2" order-md="1">
							<v-btn outlined block :disabled="cards.length === 0" @click="next(false)">
								I did not get it
							</v-btn>
						</v-col>
						<v-col class="flex-shrink-1" order="1" order-md="2">
							<v-btn
								outlined
								block
								:disabled="cards.length === 0"
								@click="showDefinition = !showDefinition"
							>
								Show definition
							</v-btn>
						</v-col>
						<v-col class="flex-shrink-1" order="3" order-md="3">
							<v-btn outlined block :disabled="cards.length === 0" @click="next(true)">
								I got it
							</v-btn>
						</v-col>
					</v-row>
				</v-col>
			</v-row>
		</div>
	</v-container>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
	data() {
		return {
			showDefinition: false,
			removeType: '',
			cards: [
				{
					phrase: 'Word 1',
					status: undefined,
					definition:
						'Laboris nulla pariatur quis commodo quis veniam velit quis nostrud officia. Labore id mollit id commodo amet ad non sint cillum reprehenderit veniam. Do qui dolore occaecat nostrud non tempor commodo duis. Sit aliqua incididunt sint elit ad commodo. Veniam mollit irure aliquip elit minim aute eiusmod nisi id minim ex deserunt ut. Tempor est ullamco culpa sint quis nisi culpa do reprehenderit.',
				},
				{
					phrase: 'Word 2',
					status: undefined,
					definition:
						'Laboris nulla pariatur quis commodo quis veniam velit quis nostrud officia. Labore id mollit id commodo amet ad non sint cillum reprehenderit veniam. Do qui dolore occaecat nostrud non tempor commodo duis. Sit aliqua incididunt sint elit ad commodo. Veniam mollit irure aliquip elit minim aute eiusmod nisi id minim ex deserunt ut. Tempor est ullamco culpa sint quis nisi culpa do reprehenderit.',
				},
				{
					phrase: 'Word 3',
					status: undefined,
					definition:
						'Laboris nulla pariatur quis commodo quis veniam velit quis nostrud officia. Labore id mollit id commodo amet ad non sint cillum reprehenderit veniam. Do qui dolore occaecat nostrud non tempor commodo duis. Sit aliqua incididunt sint elit ad commodo. Veniam mollit irure aliquip elit minim aute eiusmod nisi id minim ex deserunt ut. Tempor est ullamco culpa sint quis nisi culpa do reprehenderit.',
				},
				{
					phrase: 'Word 4',
					status: undefined,
					definition:
						'Laboris nulla pariatur quis commodo quis veniam velit quis nostrud officia. Labore id mollit id commodo amet ad non sint cillum reprehenderit veniam. Do qui dolore occaecat nostrud non tempor commodo duis. Sit aliqua incididunt sint elit ad commodo. Veniam mollit irure aliquip elit minim aute eiusmod nisi id minim ex deserunt ut. Tempor est ullamco culpa sint quis nisi culpa do reprehenderit.',
				},
			] as {
				phrase: string
				definition: string
				status?: 'correct' | 'wrong'
			}[],
		}
	},
	computed: {
		status() {
			// TODO: return based on bin value 'you have no more words to review; you are permanently done!' || 'You are temporarily done; please come back later to review more words.'
			return 'No Cards Available'
		},
	},
	methods: {
		next(correct: boolean) {
			this.cards[this.cards.length - 1].status = correct ? 'correct' : 'wrong'
			setTimeout(() => {
				this.cards.pop()
			}, 700)
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
