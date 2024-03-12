<script lang="ts">
	import * as Tabs from '$lib/components/ui/tabs'
	import { IMAGE_NAMES } from '../../api'
	import { dataset, selected_name } from '../../stores'
	import DatasetSelector from './DatasetSelector.svelte'
	import ImageTabContent from './ImageTabContent.svelte'
	import ParamSelector from './ParamSelector.svelte'
	import Separator from './ui/separator/separator.svelte'
	$: name = IMAGE_NAMES[$dataset][0]

	$: selected_name.set(name)
</script>

<Tabs.Root bind:value={name} class="flex h-screen w-full flex-col space-y-3 p-3">
	<div class="flex flex-row space-x-3">
		<ParamSelector />
		<DatasetSelector />
		<Tabs.List>
			{#each IMAGE_NAMES[$dataset] as name}
				<Tabs.Trigger value={name}>{name}</Tabs.Trigger>
			{/each}
		</Tabs.List>
	</div>
	<Separator />
	{#each IMAGE_NAMES[$dataset] as name}
		<Tabs.Content value={name} class="min-h-0 flex-1 focus-visible:flex">
			<ImageTabContent imageName={name} />
		</Tabs.Content>
	{/each}
</Tabs.Root>
