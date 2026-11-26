import './globals.css';
import './experience.css';
export const viewport = { themeColor: '#171021' };
export const metadata = { metadataBase: new URL('https://velunova.vercel.app'), icons: { icon: '/assets/favicon.svg' } };
export default function RootLayout({ children }) {
  return <html lang="en"><body>{children}</body></html>;
}
