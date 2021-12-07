<template>
	<div class="flashcard" :class="{ flip: focused ? flipped : false }">
		<v-card
			:width="width"
			:color="focused ? 'primary' : 'white'"
			elevation="5"
			max-width="500px"
			height="250px"
			class="front"
		>
			<v-row no-gutters justify="center" align="center" class="fill-height pa-5">
				<div class="text-h3 font-weight-light">{{ front }}</div>
			</v-row>
		</v-card>
		<v-card
			:width="width"
			elevation="5"
			max-width="500px"
			height="250px"
			color="secondary"
			class="back"
		>
			<v-row no-gutters justify="center" align="center" class="fill-height pa-5">
				<div class="body-1 font-weight-light text-align white--text">{{ back }}</div>
			</v-row>
		</v-card>
	</div>
</template>

<script>
export default {
	props: {
		front: {
			type: String,
			required: true,
		},
		back: {
			type: String,
			required: true,
		},
		flipped: {
			type: Boolean,
			default: false,
		},
		width: {
			type: String,
			required: false,
			default: undefined,
		},
		focused: {
			type: Boolean,
			required: false,
			default: false,
		},
	},
}
</script>

<style lang="sass">
.flashcard
	position: relative
	max-width: 500px
	height: 250px

	transition: transform 1s
	transform-style: preserve-3d

	&.flip
		transform: rotateY( 180deg )
		transition: transform 0.5s

	.front,
	.back
		position: absolute
		height: 100%
		width: 100%
		backface-visibility: hidden

	.back
		transform: rotateY( 180deg )
</style>
