<template>
	<v-card>
		<v-card-title>{{ card.phrase }}</v-card-title>
		<v-card-text>
			{{ card.definition }}
		</v-card-text>
		<v-card-subtitle>
			<ul>
				<li>
					<span class="font-weight-bold">Current Bin</span>
					<span>{{ card.currentBin.bin }}</span>
				</li>
				<li>
					<span class="font-weight-bold">Will appear</span>
					<span>{{ nextAppearance }}</span>
				</li>
				<li>
					<span class="font-weight-bold">No. incorrect</span>
					<span>{{ card.noOfIncorrect }}</span>
				</li>
			</ul>
		</v-card-subtitle>
	</v-card>
</template>

<script lang="ts">
import Vue from 'vue'
import Moment from 'moment'

export default Vue.extend({
	name: 'my-card',
	props: {
		card: {
			type: Object,
			required: true,
		},
	},
	computed: {
		nextAppearance() {
			const M = Moment(this.card.binUpdatedAt)
			const interval = this.card.currentBin.interval

			M.add(interval)

			return M.fromNow()
		},
	},
})
</script>
