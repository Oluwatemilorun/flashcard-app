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
					<span>{{ card.current_bin.bin }}</span>
				</li>
				<li>
					<span class="font-weight-bold">Will appear</span>
					<span>{{ nextAppearance }}</span>
				</li>
				<li>
					<span class="font-weight-bold">No. incorrect</span>
					<span>{{ card.no_incorrect }}</span>
				</li>
			</ul>
		</v-card-subtitle>
	</v-card>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue'
import Moment from 'moment'
import { Flashcard } from '~/types/interfaces'

export default Vue.extend({
	name: 'my-card',
	props: {
		card: {
			type: Object as PropType<Flashcard>,
			required: true,
		},
	},
	computed: {
		nextAppearance() {
			const M = Moment(this.card.bin_updated_at)
			const interval = this.card.current_bin.interval

			if (interval < 0) {
				M.add(interval)

				return M.fromNow()
			} else {
				return 'Never'
			}
		},
	},
})
</script>
