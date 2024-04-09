<script lang="ts">
	import * as Select from './ui/select'
	import { ascending, barSorting, sorting, toggleBars } from '../../stores'
	import Button from './ui/button/button.svelte'

	$: selected = { value: $sorting }

	$: sorting.set(selected.value)

	$: selectedBarSort = { value: $barSorting }

	$: barSorting.set(selectedBarSort.value)
</script>

<div class="flex space-x-3">
	{#if !$toggleBars}
		<Select.Root bind:selected>
			<Select.Trigger class="w-[180px]">
				<Select.Value placeholder="Sort by" />
			</Select.Trigger>
			<Select.Content>
				<Select.Item value="None">None</Select.Item>
				<Select.Item value="area">area</Select.Item>
				<Select.Item value="stability_score">stability_score</Select.Item>
				<Select.Item value="predicted_iou">predicted_iou</Select.Item>
				<Select.Item value="class_id">class_id</Select.Item>
			</Select.Content>
		</Select.Root>
	{:else}
		<Select.Root bind:selected={selectedBarSort}>
			<Select.Trigger class="w-[200px]">
				<Select.Value placeholder="Sort by" />
			</Select.Trigger>
			<Select.Content>
				<Select.Item value="None">None</Select.Item>
				<Select.Item value="after_sam">after_sam</Select.Item>
				<Select.Item value="after_min_area_filter">after_min_area_filter</Select.Item>
				<Select.Item value="after_iou_filter">after_iou_filter</Select.Item>
				<Select.Item value="removed_by_min_area">removed_by_min_area</Select.Item>
				<Select.Item value="removed_by_iou_thresh">removed_by_iou_thresh</Select.Item>
			</Select.Content>
		</Select.Root>
	{/if}
	<Button variant="outline" on:click={() => ascending.update((value) => !value)}>
		<svg
			class={$ascending ? 'scale-y-[-1]' : ''}
			xmlns="http://www.w3.org/2000/svg"
			width="24"
			height="24"
			viewBox="0 0 24 24"
		>
			<path fill="black" d="M3 18v-2h6v2zm0-5v-2h12v2zm0-5V6h18v2z" />
		</svg>
	</Button>
</div>
