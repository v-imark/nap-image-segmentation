<script lang="ts">
	import * as ToggleGroup from '$lib/components/ui/toggle-group/index.js'
	import { strategy, strategyKey } from '../../stores'
	import InfoTooltip from './InfoTooltip.svelte'
	import Label from './ui/label/label.svelte'
	import * as Select from './ui/select'
	import * as Tooltip from './ui/tooltip'

	let strategys = ['index', 'filter', 'value']
	let texts = [
		'Color gets selected by index of mask',
		'Color gets selected by which filter it was removed by',
		'Color gets selected by a score value (area, predicted_iou. stability_score)'
	]
</script>

<div class="flex basis-1/2 flex-col space-y-2">
	<InfoTooltip text="Select which color coding to use when choosing the color for a mask">
		<Label class="text-lg">Color Coding</Label>
	</InfoTooltip>
	<ToggleGroup.Root bind:value={$strategy} type="single" variant="outline">
		{#each strategys as strategy, i}
			<Tooltip.Root>
				<Tooltip.Trigger>
					<ToggleGroup.Item
						value={strategy}
						aria-label="Toggle {strategy}"
						class="data-[state=on]:bg-primary data-[state=on]:text-primary-foreground flex w-24 flex-col space-y-1 py-1 uppercase"
					>
						{strategy}
					</ToggleGroup.Item>
				</Tooltip.Trigger>
				<Tooltip.Content>
					<p>{texts[i]}</p>
				</Tooltip.Content>
			</Tooltip.Root>
		{/each}
	</ToggleGroup.Root>
	<Select.Root bind:selected={$strategyKey} disabled={$strategy != 'value'}>
		<Select.Trigger class="w-full">
			<Select.Value placeholder="Strategy key" />
		</Select.Trigger>
		<Select.Content>
			<Select.Item value="predicted_iou">predicted_iou</Select.Item>
			<Select.Item value="stability_score">stability_score</Select.Item>
			<Select.Item value="area">area</Select.Item>
		</Select.Content>
	</Select.Root>
</div>
