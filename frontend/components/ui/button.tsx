import { cn } from "@/lib/utils"
 interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    variant?: "default" | "outline" | "ghost" | "link"
    size?: "sm" | "md" | "lg"
    className?: string
 }

 export function Button({ className, variant = "default", size = "md", ...props }: ButtonProps) {
    return (
      <button className={cn(
        "inline-flex items-center justify-center rounded-lg font-medium transition-colors disabled:opacity-50",
        variant === "default" && "bg-gray-900 text-white hover:bg-gray-700",
        variant === "outline" && "border border-gray-200 bg-white hover:bg-gray-50",
        variant === "ghost" && "hover:bg-gray-100",
        variant === "link" && "text-primary underline-offset-4 hover:underline",
        size === "sm" && "h-8 px-3 text-sm",
        size === "md" && "h-10 px-4 text-sm",
        size === "lg" && "h-12 px-6 text-base",
        className
      )} {...props} />
    )
  }