module.exports = {
	root: true,
	env: {
		browser: true,
		node: true,
	},
	extends: [
		'@nuxtjs/eslint-config-typescript',
		'plugin:nuxt/recommended',
		'plugin:prettier/recommended',
	],
	plugins: [],
	// add your custom rules here
	rules: {
		'no-console': 'warn',
		'vue/component-name-in-template-casing': ['warn', 'kebab-case'],
		'vue/component-definition-name-casing': ['error', 'kebab-case'],
		'vue/max-attributes-per-line': [
			'warn',
			{
				singleline: 5,
				multiline: {
					max: 2,
					allowFirstLine: false,
				},
			},
		],
	},
}
