import react from '@vitejs/plugin-react';
import path from 'path';
import { defineConfig } from 'vite';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base: '/',
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  server: {
    host: '0.0.0.0', // Set this to 0.0.0.0 or true to listen on all addresses, including LAN and public addresses.
    port: 5173,
    origin: 'http://localhost:5173' // Defines the origin of the generated asset URLs during development.
  }
});
