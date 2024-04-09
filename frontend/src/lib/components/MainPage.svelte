<script lang="ts">
	import * as Tabs from '$lib/components/ui/tabs'
	import { barData, dataset, toggleBars, toggleTable } from '../../stores'
	import DatasetSelector from './DatasetSelector.svelte'
	import FilteringBar from './FilteringBar.svelte'
	import FilteringChart from './FilteringChart.svelte'
	import ImageTabContent from './ImageTabContent.svelte'
	import ParamSelector from './ParamSelector.svelte'
	import SortingSelect from './SortingSelect.svelte'
	import Label from './ui/label/label.svelte'

	import { Separator } from './ui/separator'
	import { Toggle } from './ui/toggle'
</script>

<Tabs.Root value={$dataset} class="flex h-screen w-full flex-col space-y-3 p-3">
	<div class="flex flex-row space-x-3">
		<ParamSelector />
		<DatasetSelector />
		<Toggle bind:pressed={$toggleTable} variant="outline" aria-label="Toggle italic">
			<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 256 256">
				<path
					fill="black"
					d="M224 48H32a8 8 0 0 0-8 8v136a16 16 0 0 0 16 16h176a16 16 0 0 0 16-16V56a8 8 0 0 0-8-8M40 112h40v32H40Zm56 0h120v32H96Zm120-48v32H40V64ZM40 160h40v32H40Zm176 32H96v-32h120z"
				/>
			</svg>
		</Toggle>
		<Toggle bind:pressed={$toggleBars} variant="outline" aria-label="Toggle italic">
			<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
				><path
					fill="black"
					d="M20 13.75a.75.75 0 0 0-.75-.75h-3a.75.75 0 0 0-.75.75v6.75H14V4.25c0-.728-.002-1.2-.048-1.546c-.044-.325-.115-.427-.172-.484c-.057-.057-.159-.128-.484-.172C12.949 2.002 12.478 2 11.75 2c-.728 0-1.2.002-1.546.048c-.325.044-.427.115-.484.172c-.057.057-.128.159-.172.484c-.046.347-.048.818-.048 1.546V20.5H8V8.75A.75.75 0 0 0 7.25 8h-3a.75.75 0 0 0-.75.75V20.5H1.75a.75.75 0 0 0 0 1.5h20a.75.75 0 0 0 0-1.5H20z"
				/></svg
			>
		</Toggle>
		<SortingSelect />
	</div>
	<Separator />
	{#await $barData}
		loading...
	{:then data}
		{#if $toggleBars}
			<div class="flex h-full w-min flex-col justify-evenly space-y-3">
				<Label class="text-2xl">oxford_flowers102</Label>
				<FilteringChart data={data.oxford_flowers102} />
				<Label class="text-2xl">imagenet2012</Label>
				<FilteringChart data={data.imagenet2012} />
			</div>
		{:else}
			<Tabs.Content value={'oxford_flowers102'} class="min-h-0 flex-1 focus-visible:flex">
				<ImageTabContent data={data.oxford_flowers102} dataset="oxford_flowers102" />
			</Tabs.Content>
			<Tabs.Content value={'imagenet2012'} class="min-h-0 flex-1 focus-visible:flex">
				<ImageTabContent data={data.imagenet2012} dataset="imagenet2012" />
			</Tabs.Content>
		{/if}
	{/await}
</Tabs.Root>
