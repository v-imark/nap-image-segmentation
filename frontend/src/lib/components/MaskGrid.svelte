<script lang="ts">
	import { getRelativePath, sortMasks } from '../../api'
	import { ascending, sorting } from '../../stores'
	import { COLORS, type MetadataObject } from '../../types'

	export let metaData: MetadataObject

	$: sortedData = sortMasks(metaData, $sorting, $ascending)
</script>

<div class="flex flex-wrap justify-center space-x-3 space-y-3 pb-3">
	{#each sortedData.masks as mask}
		{#key `${mask.class_id}`}
			<img
				src={`${getRelativePath(mask?.path)}/${mask?.name}`}
				alt={mask?.name}
				class="h-24 object-scale-down object-center {COLORS[
					mask.class_id
				]} ring-4 first:ml-3 first:mt-3"
			/>
		{/key}
	{/each}
</div>
