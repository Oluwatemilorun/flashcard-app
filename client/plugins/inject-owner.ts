import { Context } from '@nuxt/types'
import { getOwnerId } from '~/utils/localstorage'
import { RH_OWNER_ID } from '~/utils/constants'

export default ({ $axios }: Context) => {
	$axios.onRequest((config) => {
		const ownerId = getOwnerId()
		if (ownerId) {
			config.headers[RH_OWNER_ID] = ownerId
		}
	})
}
