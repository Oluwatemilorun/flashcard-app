<template>
	<v-container fill-height>
		<v-row justify="center" align="center" class="fill-height">
			<v-col cols="10" md="8" lg="6" class="flashcard-wrapper">
				<div v-for="(card, i) in cards" :key="i" class="flashcard-stacker">
					<flash-card
						:front="card.phrase"
						:back="card.definition"
						:flipped="showDefinition"
						:focused="cards.length - 1 === i"
						class="mx-auto"
					></flash-card>
				</div>
			</v-col>
		</v-row>

		<div class="controls-wrapper py-5">
			<v-row no-gutters justify="center" align="center">
				<v-col cols="10" md="8" lg="6">
					<v-row>
						<v-col class="flex-shrink-1">
							<v-btn outlined block>I did not get it</v-btn>
						</v-col>
						<v-col class="flex-shrink-1">
							<v-btn outlined block @click="showDefinition = !showDefinition">
								Show definition
							</v-btn>
						</v-col>
						<v-col class="flex-shrink-1">
							<v-btn outlined block>I got it</v-btn>
						</v-col>
					</v-row>
				</v-col>
			</v-row>
		</div>
	</v-container>
</template>

<script lang="ts">
export default {
	data() {
		return {
			showDefinition: false,
			cards: [
				{
					phrase: 'Word 1',
					definition:
						'Laboris nulla pariatur quis commodo quis veniam velit quis nostrud officia. Labore id mollit id commodo amet ad non sint cillum reprehenderit veniam. Do qui dolore occaecat nostrud non tempor commodo duis. Sit aliqua incididunt sint elit ad commodo. Veniam mollit irure aliquip elit minim aute eiusmod nisi id minim ex deserunt ut. Tempor est ullamco culpa sint quis nisi culpa do reprehenderit.',
				},
				{
					phrase: 'Word 2',
					definition:
						'Laboris nulla pariatur quis commodo quis veniam velit quis nostrud officia. Labore id mollit id commodo amet ad non sint cillum reprehenderit veniam. Do qui dolore occaecat nostrud non tempor commodo duis. Sit aliqua incididunt sint elit ad commodo. Veniam mollit irure aliquip elit minim aute eiusmod nisi id minim ex deserunt ut. Tempor est ullamco culpa sint quis nisi culpa do reprehenderit.',
				},
				{
					phrase: 'Word 3',
					definition:
						'Laboris nulla pariatur quis commodo quis veniam velit quis nostrud officia. Labore id mollit id commodo amet ad non sint cillum reprehenderit veniam. Do qui dolore occaecat nostrud non tempor commodo duis. Sit aliqua incididunt sint elit ad commodo. Veniam mollit irure aliquip elit minim aute eiusmod nisi id minim ex deserunt ut. Tempor est ullamco culpa sint quis nisi culpa do reprehenderit.',
				},
				{
					phrase: 'Word 4',
					definition:
						'Laboris nulla pariatur quis commodo quis veniam velit quis nostrud officia. Labore id mollit id commodo amet ad non sint cillum reprehenderit veniam. Do qui dolore occaecat nostrud non tempor commodo duis. Sit aliqua incididunt sint elit ad commodo. Veniam mollit irure aliquip elit minim aute eiusmod nisi id minim ex deserunt ut. Tempor est ullamco culpa sint quis nisi culpa do reprehenderit.',
				},
			],
		}
	},
}
</script>

<style lang="sass">
.flashcard-wrapper
	position: relative
	display: contents

.flashcard-stacker
	position: absolute
	left: 0
	right: 0
	margin: 0 auto

	transition: all 100ms ease-in-out

.controls-wrapper
	position: absolute
	left: 0
	right: 0
	bottom: 0
</style>
