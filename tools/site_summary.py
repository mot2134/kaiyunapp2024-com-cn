import json
import datetime

# 站点基础资料
SITE_DATA = {
    "name": "云开平台",
    "url": "https://www.kaiyunapp2024.com.cn",
    "keywords": ["云开", "娱乐", "体育", "电竞", "真人"],
    "tags": ["游戏", "在线娱乐", "云开官方"],
    "description": "云开平台提供全面的体育赛事、电子竞技及真人娱乐服务，致力于为用户打造安全、公正、便捷的在线娱乐环境。"
}

def format_summary(data: dict) -> str:
    """根据站点资料生成结构化的文本摘要"""
    lines = []
    lines.append("=" * 48)
    lines.append(f"站点名称：{data['name']}")
    lines.append(f"站点URL ：{data['url']}")
    lines.append("-" * 48)
    lines.append("核心关键词：")
    for kw in data["keywords"]:
        lines.append(f"  · {kw}")
    lines.append("-" * 48)
    lines.append("标签：")
    for tag in data["tags"]:
        lines.append(f"  # {tag}")
    lines.append("-" * 48)
    lines.append(f"简介：{data['description']}")
    lines.append("=" * 48)
    lines.append(f"生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return "\n".join(lines)

def export_json(data: dict) -> str:
    """输出结构化的JSON格式摘要，便于程序读取"""
    export = {
        "site_name": data["name"],
        "url": data["url"],
        "keywords": data["keywords"],
        "tags": data["tags"],
        "description": data["description"],
        "generated_at": datetime.datetime.now().isoformat()
    }
    return json.dumps(export, ensure_ascii=False, indent=2)

def export_markdown(data: dict) -> str:
    """输出Markdown格式文档摘要"""
    lines = []
    lines.append(f"# {data['name']}")
    lines.append(f"")
    lines.append(f"- **站点URL**: [{data['url']}]({data['url']})")
    lines.append(f"- **核心关键词**: {', '.join(data['keywords'])}")
    lines.append(f"- **标签**: {', '.join(data['tags'])}")
    lines.append(f"")
    lines.append(f"## 简介")
    lines.append(f"")
    lines.append(f"{data['description']}")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"*生成时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    return "\n".join(lines)

def main():
    """主程序：展示所有格式的摘要输出"""
    print("\n>>> 纯文本摘要 <<<\n")
    print(format_summary(SITE_DATA))

    print("\n\n>>> JSON 摘要 <<<\n")
    print(export_json(SITE_DATA))

    print("\n\n>>> Markdown 摘要 <<<\n")
    print(export_markdown(SITE_DATA))

    # 同时将JSON写入文件，便于GitHub预览
    output_path = "site_summary_output.json"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(export_json(SITE_DATA))
    print(f"\n\nJSON 文件已写入: {output_path}")

if __name__ == "__main__":
    main()