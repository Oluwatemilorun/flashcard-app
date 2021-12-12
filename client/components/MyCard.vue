<template>
	<v-card>
		<v-card-title class="text-capitalize">{{ card.phrase }}</v-card-title>
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
					<span>{{ card.no_wrong }}</span>
				</li>
			</ul>
		</v-card-subtitle>
	</v-card>
</template>

<script lang="ts">
import Vue from 'vue'
import type { PropType } from 'vue'
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
			const m = Moment.utc(this.card.bin_updated_at)
			const interval = (this.card as Flashcard).current_bin.interval

			if (interval >= 0) {
				m.add(interval)
				const now = m.fromNow()

				return now.toLowerCase().includes('ago') ? 'Now' : now
			} else {
				return 'Never'
			}
		},
	},
})
</script>
