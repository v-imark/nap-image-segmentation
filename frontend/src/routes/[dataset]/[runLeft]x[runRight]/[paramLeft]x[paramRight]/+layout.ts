import { getMetaDataUrl } from '../../../../api'
import type { MetadataObject } from '../../../../types'
import type { LayoutLoad } from './$types'

export const load: LayoutLoad = async ({ fetch, params }) => {
	const url = getMetaDataUrl(params.paramLeft, params.dataset, params.runLeft)
	const left: MetadataObject[] = await fetch(`${url}/metadata.json`).then((res) => {
		return res.status != 404 ? res.json() : []
	})
	const url2 = getMetaDataUrl(params.paramRight, params.dataset, params.runRight)
	const right: MetadataObject[] = await fetch(`${url2}/metadata.json`).then((res) => {
		return res.status != 404 ? res.json() : []
	})

	return {
		right: right,
		left: left
	}
}
