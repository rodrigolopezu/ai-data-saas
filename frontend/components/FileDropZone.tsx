"use client"

import { useCallback, useState } from "react"
import { cn } from "@/lib/utils"

interface FileDropzoneProps {
  onFileSelect: (file: File) => void
  isLoading?: boolean
}

export function FileDropzone({ onFileSelect, isLoading = false }: FileDropzoneProps) {
  const [isDragging, setIsDragging] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const validateFile = (file: File): string | null => {
    const validTypes = [
      "text/csv",
      "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "application/vnd.ms-excel",
    ]
    if (!validTypes.includes(file.type)) {
      return "Solo se aceptan archivos CSV o Excel (.xlsx, .xls)"
    }
    if (file.size > 10 * 1024 * 1024) {
      return "El archivo no puede superar los 10MB"
    }
    return null
  }

  const handleFile = useCallback((file: File) => {
    const validationError = validateFile(file)
    if (validationError) {
      setError(validationError)
      return
    }
    setError(null)
    onFileSelect(file)
  }, [onFileSelect])

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault()
    setIsDragging(false)
    const file = e.dataTransfer.files[0]
    if (file) handleFile(file)
  }, [handleFile])

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault()
    setIsDragging(true)
  }

  const handleDragLeave = () => setIsDragging(false)

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) handleFile(file)
  }

  return (
    <div className="w-full">
      <label
        className={cn(
          "flex flex-col items-center justify-center w-full h-64 rounded-xl border-2 border-dashed cursor-pointer transition-all duration-200",
          isDragging
            ? "border-gray-900 bg-gray-50 scale-[1.02]"
            : "border-gray-300 bg-white hover:border-gray-400 hover:bg-gray-50",
          isLoading && "opacity-50 cursor-not-allowed"
        )}
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
      >
        <div className="flex flex-col items-center justify-center gap-3 text-center px-6">
          <div className={cn(
            "w-14 h-14 rounded-full flex items-center justify-center transition-colors",
            isDragging ? "bg-gray-900" : "bg-gray-100"
          )}>
            <svg
              className={cn("w-6 h-6", isDragging ? "text-white" : "text-gray-500")}
              fill="none" viewBox="0 0 24 24" stroke="currentColor"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
            </svg>
          </div>
          <div>
            <p className="text-sm font-medium text-gray-700">
              {isDragging ? "Suelta el archivo aquí" : "Arrastra tu archivo aquí"}
            </p>
            <p className="text-xs text-gray-400 mt-1">
              o haz clic para seleccionar
            </p>
          </div>
          <p className="text-xs text-gray-400">
            CSV, XLSX o XLS · Máximo 10MB
          </p>
        </div>
        <input
          type="file"
          className="hidden"
          accept=".csv,.xlsx,.xls"
          onChange={handleInputChange}
          disabled={isLoading}
        />
      </label>

      {error && (
        <p className="mt-3 text-sm text-red-600 flex items-center gap-1">
          <span>⚠</span> {error}
        </p>
      )}
    </div>
  )
}