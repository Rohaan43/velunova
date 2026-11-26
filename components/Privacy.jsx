'use client';
import { useRef } from 'react';
export default function Privacy() {
  const dialogRef = useRef(null);
  function closeOnBackdrop(event) {
    const dialog = dialogRef.current;
    const rect = dialog.getBoundingClientRect();
    if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
  }
  return <><button className="privacy-button" type="button" onClick={() => dialogRef.current.showModal()}>Privacy</button><dialog ref={dialogRef} onClick={closeOnBackdrop} id="privacy-dialog" aria-labelledby="privacy-title"><button className="dialog-close" onClick={() => dialogRef.current.close()} type="button" aria-label="Close privacy information">{"×"}</button><p className="eyebrow">{"Your privacy"}</p><h2 id="privacy-title">{"Your ideas stay yours."}</h2><p>{"The project brief form creates a text file on your device. Your answers are not transmitted to Velunova, saved to a database, or stored in your browser by this website."}</p><p>{"This website does not use analytics or advertising cookies. Fonts and artwork are hosted with the site. The hosting provider may process standard request information to deliver the website."}</p><p>{"When you share your downloaded brief separately, the privacy terms of your chosen communication channel apply."}</p></dialog></>;
}
