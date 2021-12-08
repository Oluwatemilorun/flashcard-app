<template>
	<v-container>
		<v-row no-gutters>
			<v-col cols="12">
				<v-row class="mt-15 mb-5" align="center">
					<v-col class="flex-grow-1">
						<h3 class="text-h4">My Cards</h3>
					</v-col>
					<v-col cols="4" class="flex-shrink-0">
						<v-btn outlined>
							<v-icon>mdi-plus</v-icon>
							Create New Card
						</v-btn>
					</v-col>
				</v-row>
			</v-col>
			<v-col cols="12">
				<v-row>
					<template v-for="(card, index) in cards">
						<v-col :key="index" cols="12" sm="2" md="3" lg="4">
							<my-card :card="card"></my-card>
						</v-col>
					</template>
				</v-row>
			</v-col>
		</v-row>
	</v-container>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
	layout: 'backdoor',
	data() {
		return {
			cards: [
				{
					phrase: 'Word 1',
					status: undefined,
					noOfIncorrect: 3,
					binUpdatedAt: '2021-12-08T15:35:56.697Z',
					currentBin: {
						bin: 3,
						interval: 5000000,
					},
					definition:
						'Laboris nulla pariatur quis commodo quis veniam velit quis nostrud officia. Labore id mollit id commodo amet ad non sint cillum reprehenderit veniam. Do qui dolore occaecat nostrud non tempor commodo duis. Sit aliqua incididunt sint elit ad commodo. Veniam mollit irure aliquip elit minim aute eiusmod nisi id minim ex deserunt ut. Tempor est ullamco culpa sint quis nisi culpa do reprehenderit.',
				},
			],
		}
	},
})
</script>
