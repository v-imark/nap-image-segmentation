<script lang="ts">
	import { page } from '$app/stores'
	import { getImageUrl } from '../../api'
	import { selectedImages } from '../../stores'
	import type { Dataset } from '../../types'
	import * as Select from './ui/select'
	export let dataset: Dataset = 'oxford_flowers102'
	export let imageNames: string[]
	$: selected = $selectedImages.map((name) => ({ value: name }))
</script>

<Select.Root
	{selected}
	onSelectedChange={(vals) => {
		if (vals) {
			$selectedImages = vals.map((val) => val.value)
		} else {
			$selectedImages = []
		}
	}}
	multiple
>
	<Select.Trigger class="w-72">
		<div>Selected images: {$selectedImages.length}</div>
	</Select.Trigger>
	<Select.Content class="max-h-[800px] overflow-y-auto">
		{#each imageNames as name}
			<Select.Item value={name}>
				<img
					src={getImageUrl(name, dataset, $page.params.run, imageNames)}
					alt={name}
					class="h-[120px] w-[120px] object-contain"
				/>
			</Select.Item>
		{/each}
	</Select.Content>
</Select.Root>
