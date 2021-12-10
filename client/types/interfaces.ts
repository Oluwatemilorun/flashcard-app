/* eslint-disable camelcase */

export interface Bin {
	bin: number
	id: string
	interval: number
}

export interface Flashcard {
	bin_updated_at: string
	created_at: string
	current_bin: Bin
	definition: string
	id: string
	no_correct: number
	no_wrong: number
	owner: string
	phrase: string
	updated_at: string
}
