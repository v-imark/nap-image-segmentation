import type { LayoutLoad } from './$types'

export const load: LayoutLoad = async ({ fetch, params }) => {
	const imagenet: string[] = await fetch(
		`http://localhost:5173/data/${params.run}/images/imagenet2012/image_names.json`
	).then((val) => val.json())
	const oxford: string[] = await fetch(
		`http://localhost:5173/data/${params.run}/images/oxford_flowers102/image_names.json`
	).then((val) => val.json())
	const oxford_pets: string[] = await fetch(
		`http://localhost:5173/data/${params.run}/images/oxford_iiit_pet/image_names.json`
	).then((val) => val.json())

	return {
		imageNames: {
			imagenet2012: imagenet,
			oxford_flowers102: oxford,
			oxford_iiit_pet: oxford_pets
		}
	}
}
