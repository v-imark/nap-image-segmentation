<script lang="ts">
	import { formatBarData, formatBarDataForDataset, getSpan } from '../../api'
	import { barData, dataset } from '../../stores'
	import { Label } from './ui/label'
	import FilteringChart from './FilteringChart.svelte'
	import FilteringBar from './FilteringBar.svelte'
</script>

{#await $barData then data}
	<div class="flex w-full flex-row">
		<FilteringChart data={data[$dataset]} />
	</div>
{/await}
