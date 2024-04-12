<script lang="ts">
	import { getRelativePath, sortMasks } from '../../api'
	import { ascending, sorting } from '../../stores'
	import { BG_COLORS, COLORS, type MetadataObject } from '../../types'
	import * as Table from './ui/table'

	export let data: MetadataObject
	export let probabilityView = false
	export let hovered = ''
	$: sortedData = sortMasks(data, $sorting, $ascending)
	$: console.log(hovered)
	let style = (mask: any) =>
		`${BG_COLORS[mask.class_id]} bg-opacity-30 hover:${
			BG_COLORS[mask.class_id]
		} hover:bg-opacity-45`
</script>

<Table.Root class="h-full overflow-y-auto" on:mouseleave={() => (hovered = '')}>
	<Table.Caption class="caption-top text-left">
		After SAM: {sortedData.segmentation_info.after_sam}, After min-area: {sortedData
			.segmentation_info.after_min_area_filter}, After IoU: {sortedData.segmentation_info
			.after_iou_filter}
	</Table.Caption>
	<Table.Header class="sticky top-0 bg-white">
		<Table.Row>
			<Table.Head>Mask</Table.Head>
			<Table.Head>Area</Table.Head>
			<Table.Head>Predicted IoU</Table.Head>
			<Table.Head>Stability Score</Table.Head>
		</Table.Row>
	</Table.Header>
	<Table.Body>
		{#each sortedData.masks as mask}
			<Table.Row
				class={probabilityView ? '' : style(mask)}
				on:mouseenter={() => {
					console.log(mask.name)
					hovered = mask.name
				}}
			>
				<Table.Cell>
					<img
						src={`${getRelativePath(mask.path)}/${mask.name}`}
						alt={mask.name}
						class="h-16 bg-black"
					/>
				</Table.Cell>
				<Table.Cell class="font-medium"
					>{mask.area} ({(100 * (mask.area / (mask.crop_box[2] * mask.crop_box[3]))).toFixed(
						3
					)}%)</Table.Cell
				>
				<Table.Cell class="font-medium">{mask.predicted_iou.toFixed(3)}</Table.Cell>
				<Table.Cell class="font-medium">{mask.stability_score.toFixed(3)}</Table.Cell>
			</Table.Row>
		{/each}
	</Table.Body>
</Table.Root>
