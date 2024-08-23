/** @type {import('tailwindcss').Config} */
// tailwind.config.js
module.exports = {
  content: [
    './templates/**/*.html', // Include all HTML files in the templates directory
    './static/**/*.js',      // Include any JavaScript files if you are using Tailwind classes in JS
    // Add any other file types where Tailwind classes may appear
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};


