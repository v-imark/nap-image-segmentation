<script lang="ts">
	import { FilterKeys, ParamKeys, type ParamSliderData } from '../../types'
	import ParamSlider from '$lib/components/ParamSlider.svelte'
	import { Separator } from './ui/separator'
	import Label from './ui/label/label.svelte'
	import InfoTooltip from './InfoTooltip.svelte'
	import ParamSelector from './ParamSelector.svelte'
	export let params: ParamSliderData
	export let column: number | undefined
	const paramKeys = {
		sam_params: ParamKeys,
		filters: FilterKeys
	}
	const maxMinStep = {
		sam_params: {
			points_per_side: { max: 32, min: 0, step: 4, disable: true },
			pred_iou_thresh: { max: 1.1, min: 0, step: 0.005, disable: false },
			stability_score_thresh: { max: 1.1, min: 0, step: 0.005, disable: false },
			crop_n_layers: { max: 4, min: 0, step: 1, disable: true },
			crop_n_layers_downscale_factor: { max: 5, min: 1, step: 1, disable: true }
		},
		filters: {
			min_area: { max: 1, min: 0, step: 0.005, disable: false },
			iou_thresh: { max: 1, min: 0, step: 0.005, disable: false }
		}
	}
</script>

<div class="flex w-full flex-row space-x-3">
	<div class="flex basis-1/2 flex-col space-y-3">
		<div class="flex justify-between">
			<InfoTooltip text="Change parameter setup by the select box or changing the sliders.">
				<Label class="text-lg">SAM params</Label>
			</InfoTooltip>
			{#if column != undefined}<ParamSelector {column} />{/if}
		</div>
		{#if params.sam_params?.points_per_side}
			{#each paramKeys.sam_params as paramKey}
				<ParamSlider
					bind:value={params.sam_params[paramKey]}
					label={paramKey}
					maxMinStep={maxMinStep.sam_params[paramKey]}
				/>
			{/each}
		{/if}
	</div>
	<Separator orientation="vertical" />
	<div class="flex basis-1/2 flex-col space-y-3">
		<InfoTooltip text="Apply additional filtering by moving the sliders.">
			<Label class="text-lg">Filters</Label>
		</InfoTooltip>
		{#each paramKeys.filters as paramKey}
			<ParamSlider
				bind:value={params.filters[paramKey]}
				label={paramKey}
				maxMinStep={maxMinStep.filters[paramKey]}
			/>
		{/each}
	</div>
</div>
