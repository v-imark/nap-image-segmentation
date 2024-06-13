<script lang="ts">
	import { page } from '$app/stores'
	import { getImageUrl } from '../../api'
	import { selectedImage } from '../../stores'
	import type { Dataset } from '../../types'
	import * as Select from './ui/select'
	export let dataset: Dataset = 'oxford_flowers102'
	export let imageNames: string[]
	let selected = { value: imageNames.find((name) => name == $selectedImage) ?? imageNames[0] }
</script>

<Select.Root {selected} onSelectedChange={(val) => ($selectedImage = val?.value ?? '')}>
	<Select.Trigger class={dataset == 'imagenet2012' ? 'w-64' : 'w-48'}>
		<Select.Value placeholder="Select image" />
	</Select.Trigger>
	<Select.Content class="max-h-[800px] overflow-y-auto">
		{#each imageNames as name}
			<Select.Item value={name} label={name}>
				<img
					src={getImageUrl(name, dataset, $page.params.runLeft, imageNames)}
					alt={name}
					class="h-[120px] w-[120px] object-contain"
				/>
			</Select.Item>
		{/each}
	</Select.Content>
</Select.Root>
