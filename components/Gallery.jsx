'use client';
import { useEffect, useRef, useState } from 'react';
import { projects } from '../lib/projects';
export default function Gallery({ children }) {
  const [project, setProject] = useState(null);
  const dialogRef = useRef(null);
  useEffect(() => { if (project) dialogRef.current.showModal(); }, [project]);
  function close() { dialogRef.current.close(); setProject(null); }
  function backdrop(event) {
    const rect = dialogRef.current.getBoundingClientRect();
    if (event.target === dialogRef.current && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) close();
  }
  return <div onClick={event => { const button = event.target.closest('[data-project]'); if (button && projects[button.dataset.project]) setProject(projects[button.dataset.project]); }}>
    {children}
    <dialog id="project-dialog" ref={dialogRef} aria-labelledby="dialog-title" onCancel={() => setProject(null)} onClick={backdrop}>
      <button className="dialog-close" type="button" aria-label="Close project details" onClick={close}>×</button>
      <p className="eyebrow">{project?.category}</p><h2 id="dialog-title">{project?.title}</h2><p>{project?.description}</p>
      <ul>{project?.deliverables.map(text => <li key={text}>{text}</li>)}</ul>
      <a className="button" href={project ? `/?service=${encodeURIComponent(project.service)}#project` : "#project"}>Plan a project <span aria-hidden="true">✦</span></a>
    </dialog>
  </div>;
}
