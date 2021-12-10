export default {
	head: {
		titleTemplate: '%s - Flashcard',
		title: 'Home',
		htmlAttrs: {
			lang: 'en',
		},
		meta: [
			{ charset: 'utf-8' },
			{ name: 'viewport', content: 'width=device-width, initial-scale=1' },
			{ hid: 'description', name: 'description', content: '' },
			{ name: 'format-detection', content: 'telephone=no' },
		],
		link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
	},
	css: [],
	plugins: [],
	components: true,
	buildModules: ['@nuxt/typescript-build', '@nuxtjs/vuetify'],
	modules: ['@nuxtjs/axios'],
	axios: {
		baseUrl: process.env.BASE_URL,
	},
	vuetify: {
		customVariables: ['~/assets/styles/variables.scss'],
		optionsPath: '~/configs/vuetify.config.ts',
	},

	// Build Configuration: https://go.nuxtjs.dev/config-build
	build: {},
}
