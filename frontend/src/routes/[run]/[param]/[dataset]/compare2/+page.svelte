<script lang="ts">
	import { page } from '$app/stores'
	import { formatRouteParam } from '../../../../../types'
	import type { PageData } from './$types'

	export let data: PageData

	$: dataset = formatRouteParam($page.params.dataset)
</script>

{data}
