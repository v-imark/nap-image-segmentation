<script lang="ts">
	import DatasetSelector from './DatasetSelector.svelte'
	import DisplayOptions from './DisplayOptions.svelte'
	import ParamSelector from './ParamSelector.svelte'
	import SortingSelect from './SortingSelect.svelte'
</script>

<div class="flex space-x-3">
	<ParamSelector />
	<DatasetSelector />
	<slot />
</div>
