<script lang="ts">
	import { page } from '$app/stores'
	import type { Dataset } from '../../types'
	import * as Select from './ui/select'
	export let image: string
	export let dataset: Dataset = 'oxford_flowers102'
	export let imageNames: {
		imagenet2012: string[]
		oxford_flowers102: string[]
		oxford_iiit_pet: string[]
	}

	$: selected = { value: imageNames[dataset][0] }
	$: image = selected.value
</script>

<Select.Root {selected} onSelectedChange={(val) => (image = val?.value ?? '')}>
	<Select.Trigger class={dataset == 'imagenet2012' ? 'w-64' : 'w-48'}>
		<Select.Value placeholder="Select image" />
	</Select.Trigger>
	<Select.Content>
		{#each imageNames[dataset] as name}
			<Select.Item value={name}>{name}</Select.Item>
		{/each}
	</Select.Content>
</Select.Root>
