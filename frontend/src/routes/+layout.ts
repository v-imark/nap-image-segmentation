import { getMetaDataUrl } from '../api'
import type { MetadataObject } from '../types'
import type { LayoutLoad } from './$types'

export const load: LayoutLoad = async ({ fetch }) => {
	const paramId = 'default'
	const run = 'test2'
	const url = getMetaDataUrl(paramId, 'imagenet2012', run)
	const imagenet_json: MetadataObject[] = await fetch(`${url}/metadata.json`).then((res) => {
		return res.status != 404 ? res.json() : []
	})
	const url2 = getMetaDataUrl(paramId, 'oxford_flowers102', run)
	const oxford_json: MetadataObject[] = await fetch(`${url2}/metadata.json`).then((res) => {
		return res.status != 404 ? res.json() : []
	})
	const url3 = getMetaDataUrl(paramId, 'oxford_iiit_pet', run)
	const oxford_pets_json: MetadataObject[] = await fetch(`${url3}/metadata.json`).then((res) => {
		return res.status != 404 ? res.json() : []
	})

	return {
		imagenet2012: imagenet_json,
		oxford_flowers102: oxford_json,
		oxford_iiit_pet: oxford_pets_json
	}
}
