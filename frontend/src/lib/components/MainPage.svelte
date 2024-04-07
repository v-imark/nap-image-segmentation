<script lang="ts">
	import * as Tabs from '$lib/components/ui/tabs'
	import { barData, dataset, toggleTable } from '../../stores'
	import DatasetSelector from './DatasetSelector.svelte'
	import ImageTabContent from './ImageTabContent.svelte'
	import ParamSelector from './ParamSelector.svelte'

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
	</div>
	<Separator />
	{#await $barData}
		loading...
	{:then data}
		<Tabs.Content value={'oxford_flowers102'} class="min-h-0 flex-1 focus-visible:flex">
			<ImageTabContent data={data.oxford_flowers102} dataset="oxford_flowers102" />
		</Tabs.Content>
		<Tabs.Content value={'imagenet2012'} class="min-h-0 flex-1 focus-visible:flex">
			<ImageTabContent data={data.imagenet2012} dataset="imagenet2012" />
		</Tabs.Content>
	{/await}
</Tabs.Root>
