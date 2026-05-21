"use client"

import { useState } from "react"
import { FileDropzone } from "@/components/FileDropZone"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export default function Home() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const handleFileSelect = (file: File) => {
    setSelectedFile(file)
  }

  return (
    <main className="min-h-screen bg-gray-50 flex items-center justify-center p-6">
      <div className="w-full max-w-xl">

        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900">
            AI Data Analytics
          </h1>
          <p className="mt-2 text-gray-500">
            Sube tu archivo y obtén insights automáticos en segundos
          </p>
        </div>

        {/* Card principal */}
        <Card>
          <CardHeader>
            <CardTitle>Sube tu archivo de datos</CardTitle>
          </CardHeader>
          <CardContent>
            <FileDropzone onFileSelect={handleFileSelect} />

            {/* Confirmación de archivo seleccionado */}
            {selectedFile && (
              <div className="mt-4 p-3 bg-gray-50 rounded-lg flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-gray-700">
                    {selectedFile.name}
                  </p>
                  <p className="text-xs text-gray-400">
                    {(selectedFile.size / 1024).toFixed(1)} KB
                  </p>
                </div>
                <button
                  onClick={() => setSelectedFile(null)}
                  className="text-gray-400 hover:text-gray-600 text-lg leading-none"
                >
                  ✕
                </button>
              </div>
            )}

            {/* Botón de análisis */}
            {selectedFile && (
              <button className="mt-4 w-full h-11 bg-gray-900 text-white rounded-lg text-sm font-medium hover:bg-gray-700 transition-colors">
                Analizar con IA →
              </button>
            )}
          </CardContent>
        </Card>

        <p className="text-center text-xs text-gray-400 mt-6">
          Tus datos se procesan en memoria y no se almacenan
        </p>

      </div>
    </main>
  )
}