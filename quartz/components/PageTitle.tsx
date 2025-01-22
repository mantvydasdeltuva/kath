import { pathToRoot } from "../util/path"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"
import { i18n } from "../i18n"

const PageTitle: QuartzComponent = ({ fileData, cfg, displayClass }: QuartzComponentProps) => {
  const title = cfg?.pageTitle ?? i18n(cfg.locale).propertyDefaults.title
  const subTitle = cfg?.pageSubTitle ?? ""
  const baseDir = pathToRoot(fileData.slug!)
  return (
    <div>
      <div style={{ display: "flex", flexDirection: "row", alignItems: "center", gap: "1rem", }}>
        <a href={baseDir} style={{ width: "2rem", height: "2rem" }}>
          <img src="/static/icon.png" style={{width: "2rem", margin: "0 0"}}></img>
        </a>
        <h2 class={classNames(displayClass, "page-title")}>
          <a href={baseDir}>{title}</a>
        </h2>
      </div>
      <p class={classNames(displayClass, "content-meta")}>
        {subTitle}
      </p>
    </div>
  )
}

PageTitle.css = `
.page-title {
  font-size: 1.75rem;
  margin: 0;
}
`

export default (() => PageTitle) satisfies QuartzComponentConstructor
