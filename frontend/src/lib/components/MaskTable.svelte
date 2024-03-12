<script lang="ts">
	import { getRelativePath } from '../../api'
	import { data } from '../../stores'
	import * as Table from './ui/table'
</script>

{#await $data then d}
	<Table.Root class="h-full overflow-y-auto">
		<Table.Caption class="caption-top text-left"
			>Total masks: {d.segmentation_info.initial_size}</Table.Caption
		>
		<Table.Header class="sticky top-0 bg-white">
			<Table.Row>
				<Table.Head>Mask</Table.Head>
				<Table.Head>Area</Table.Head>
				<Table.Head>Predicted IoU</Table.Head>
				<Table.Head>Stability Score</Table.Head>
			</Table.Row>
		</Table.Header>
		<Table.Body>
			{#each d.masks as mask}
				<Table.Row class="h">
					<Table.Cell>
						<img src={`${getRelativePath(mask.path)}/${mask.name}`} alt={mask.name} class="h-32" />
					</Table.Cell>
					<Table.Cell class="font-medium">{mask.area}</Table.Cell>
					<Table.Cell class="font-medium">{mask.predicted_iou}</Table.Cell>
					<Table.Cell class="font-medium">{mask.stability_score}</Table.Cell>
				</Table.Row>
			{/each}
		</Table.Body>
	</Table.Root>
{/await}
