import type { LayoutLoad } from './$types'
import { getMetaDataUrl } from '../../../../api'
import type { MetadataObject } from '../../../../types'

export const load: LayoutLoad = async ({ fetch, params }) => {
	const url = getMetaDataUrl(params.param, params.dataset, params.run)
	const metadata: MetadataObject[] = await fetch(`${url}/metadata.json`).then((res) => {
		return res.status != 404 ? res.json() : []
	})

	let totalMasks = 0
	metadata?.forEach((element) => {
		totalMasks += element.segmentation_info.after_sam
	})
	console.log(params.param, params.dataset, totalMasks)
	return {
		metadata
	}
}
