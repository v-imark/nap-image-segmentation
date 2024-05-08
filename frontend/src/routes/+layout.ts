import type { Param } from '../types'
import type { LayoutLoad } from './$types'

export const load: LayoutLoad = async ({ fetch }) => {
	const response = await fetch('http://localhost:5173/test_params.json').then((val) => val.json())

	return {
		params: response as { [key: string]: Param[] }
	}
}
