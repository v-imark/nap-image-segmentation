<script lang="ts">
	import { page } from '$app/stores'
	import { FilterKeys, ParamKeys, type MetadataObject, type ParamSliderData } from '../../types'
	import AnnotatedImage from './AnnotatedImage.svelte'
	import ParamSlider from '$lib/components/ParamSlider.svelte'
	import ParamSliders from '$lib/components/ParamSliders.svelte'
	import { Label } from './ui/label'
	import { Separator } from './ui/separator'
	import MaskTable from './MaskTable.svelte'
	export let column: number | undefined
	export let data: MetadataObject
	export let src: string
	$: params = data?.params
	let sliderParams = {
		sam_params: params,
		filters: { min_area: 0, iou_thresh: 1 }
	}
	$: sliderParams.sam_params = params
	let hovered = ''
</script>

<div class="flex h-full w-full flex-col space-y-3">
	<div class="flex h-[400px] items-center justify-center">
		<AnnotatedImage {data} {src} params={sliderParams} size={400} {hovered} />
	</div>
	<Separator />
	{#key params?.points_per_side}
		<ParamSliders bind:params={sliderParams} {column} />
	{/key}
	<Separator />
	<div class="h-56">
		<MaskTable {data} bind:hovered params={sliderParams} />
	</div>
</div>
