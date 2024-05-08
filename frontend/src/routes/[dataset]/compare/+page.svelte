<script lang="ts">
	import { page } from '$app/stores'
	import type { PageData } from './$types'
	import { formatRouteParam } from '../../../types'

	export let data: PageData

	$: dataset = formatRouteParam($page.params.dataset)
</script>

{dataset}
