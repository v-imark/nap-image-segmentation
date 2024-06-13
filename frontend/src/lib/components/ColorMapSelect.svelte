<script lang="ts">
	import * as ToggleGroup from '$lib/components/ui/toggle-group/index.js'
	import { colorMap } from '../../stores'
	import ColorMap from './ColorMap.svelte'
	import InfoTooltip from './InfoTooltip.svelte'
	import Label from './ui/label/label.svelte'

	let maps = ['jet', 'cool', 'hot']
</script>

<div class="flex basis-1/2 flex-col space-y-2">
	<InfoTooltip text="Select which color map to use">
		<Label class="text-lg">Color map</Label>
	</InfoTooltip>
	<ToggleGroup.Root bind:value={$colorMap} type="single" variant="outline">
		{#each maps as map}
			<ToggleGroup.Item
				value={map}
				aria-label="Toggle {map}"
				class="data-[state=on]:bg-primary data-[state=on]:text-primary-foreground w-24 py-2"
			>
				<ColorMap {map} />
			</ToggleGroup.Item>
		{/each}
	</ToggleGroup.Root>
</div>
