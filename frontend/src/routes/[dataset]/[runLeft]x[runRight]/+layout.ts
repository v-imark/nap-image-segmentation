import type { LayoutLoad } from './$types'

export const load: LayoutLoad = async ({ fetch, params }) => {
	const left: string[] = await fetch(
		`/data/${params.runLeft}/images/${params.dataset}/image_names.json`
	).then((val) => val.json())

	const right: string[] = await fetch(
		`/data/${params.runRight}/images/${params.dataset}/image_names.json`
	).then((val) => val.json())

	return {
		imageNames: {
			left,
			right
		}
	}
}
