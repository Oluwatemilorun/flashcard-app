<template>
	<v-app>
		<v-navigation-drawer app color="secondary">
			<v-toolbar dense>
				<v-toolbar-title>Flashcard Backdoor</v-toolbar-title>
			</v-toolbar>
			<v-list nav dark>
				<v-list-item to="/backdoor/cards"> My cards </v-list-item>
				<v-list-item to="/backdoor/bin"> Bin settings </v-list-item>
			</v-list>
		</v-navigation-drawer>

		<v-main>
			<nuxt />
		</v-main>
	</v-app>
</template>

<script lang="ts"></script>
