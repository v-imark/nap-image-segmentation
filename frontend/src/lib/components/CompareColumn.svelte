<script lang="ts">
	import { page } from '$app/stores'
	import { FilterKeys, ParamKeys, type MetadataObject, type ParamSliderData } from '../../types'
	import AnnotatedImage from './AnnotatedImage.svelte'
	import ParamSlider from '$lib/components/ParamSlider.svelte'
	import ParamSliders from '$lib/components/ParamSliders.svelte'
	import { Label } from './ui/label'
	import { Separator } from './ui/separator'

	export let data: MetadataObject
	$: params = data?.params
	let sliderParams = {
		sam_params: params,
		filters: { min_area: 0, iou_thresh: 1 }
	}
	$: sliderParams.sam_params = params
</script>

<div class="flex h-full w-full flex-col space-y-3">
	<div class="flex h-[450px] items-center justify-center">
		<AnnotatedImage {data} params={sliderParams} size={450} />
	</div>
	<Separator />
	{#key params?.points_per_side}
		<ParamSliders bind:params={sliderParams} />
	{/key}
</div>
