import { LS_OWNER_ID } from './constants'

export const setOwnerId = (id: string) => {
	if (localStorage) localStorage.setItem(LS_OWNER_ID, id)
}

export const getOwnerId = () => {
	const id = typeof localStorage !== 'undefined' ? localStorage.getItem(LS_OWNER_ID) : null

	return id
}
