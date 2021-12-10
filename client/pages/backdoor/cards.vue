<template>
	<v-container>
		<v-row no-gutters>
			<v-col cols="12">
				<v-row class="mt-15 mb-5" align="center">
					<v-col class="flex-grow-1">
						<h3 class="text-h4">My Cards</h3>
					</v-col>
					<v-col cols="4" class="flex-shrink-0">
						<v-btn outlined @click="addNewDialog = true">
							<v-icon>mdi-plus</v-icon>
							Create New Card
						</v-btn>
					</v-col>
				</v-row>
			</v-col>
			<v-col cols="12">
				<v-row v-if="loadingCards" justify="center" align="center">
					<v-progress-circular size="48" indeterminate />
				</v-row>
				<v-row v-else>
					<template v-for="(card, index) in cards">
						<v-col :key="index" cols="12" sm="2" md="3" lg="4">
							<my-card :card="card"></my-card>
						</v-col>
					</template>
				</v-row>
			</v-col>
		</v-row>

		<v-dialog v-model="addNewDialog" persistent max-width="600px">
			<v-card>
				<v-card-title>
					<span class="text-h5 px-3">Create flashcard</span>
				</v-card-title>
				<v-card-text>
					<v-container>
						<v-form v-model="addNewForm">
							<v-row>
								<v-col cols="12">
									<v-text-field
										v-model="phrase"
										label="Phrase"
										required
										outlined
										:rules="[(v) => !!v || 'Phrase is required']"
									></v-text-field>
								</v-col>
								<v-col cols="12">
									<v-textarea
										v-model="definition"
										label="Definition"
										required
										outlined
										:rules="[(v) => !!v || 'Definition is required']"
									></v-textarea>
								</v-col>
							</v-row>
						</v-form>
					</v-container>
				</v-card-text>
				<v-card-actions class="px-10 pb-4">
					<v-spacer></v-spacer>
					<v-btn text :disabled="addNewLoader" @click="close()"> Close </v-btn>
					<v-btn outlined :disabled="!addNewForm" :loading="addNewLoader" @click="saveCard()">
						Save Flashcard
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>

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
import { setOwnerId } from '~/utils/localstorage'
import { Flashcard } from '~/types/interfaces'

export default Vue.extend({
	layout: 'backdoor',
	data() {
		return {
			addNewDialog: false,
			addNewForm: false,
			addNewLoader: false,
			loadingCards: true,
			snackbar: false,
			snackbarText: '',
			phrase: '',
			definition: '',
			cards: [] as Flashcard[],
		}
	},
	mounted() {
		this.getCards()
	},
	methods: {
		close() {
			this.addNewDialog = false
			this.addNewForm = false
			this.resetForm()
		},
		async saveCard() {
			this.addNewLoader = true
			try {
				const { data } = await this.$axios.post('/v1/cards', {
					phrase: this.phrase,
					definition: this.definition,
				})

				const card = data.payload as Flashcard

				setOwnerId(card.owner)

				this.cards.push(card)
				this.close()
			} catch (error) {
				this.showSnackbar(error.response ? error.response.message : error.message)
			} finally {
				this.addNewLoader = false
			}
		},
		resetForm() {
			this.phrase = ''
			this.definition = ''
		},
		showSnackbar(message: string) {
			this.snackbarText = message
			this.snackbar = true
		},
		async getCards() {
			this.loadingCards = true
			try {
				const { data } = await this.$axios.get('/v1/cards')
				const cards = data.payload as Flashcard[]

				this.cards = cards
			} catch (error) {
				this.showSnackbar(error.response ? error.response.message : error.message)
			} finally {
				this.loadingCards = false
			}
		},
	},
})
</script>
