import sys
import os
import tempfile
import shutil

class MinHeap:
  def __init__(self):
    self.data = []

  def push(self, item):
    self.data.append(item)
    self._sobe(len(self.data) - 1)

  def pop(self):
    if len(self.data) == 0:
      return None
    self._troca(0, len(self.data) - 1)
    menor = self.data.pop()
    self._desce(0)
    return menor

  def _sobe(self, idx):
    pai = (idx - 1) // 2
    while idx > 0 and self.data[idx] < self.data[pai]:
      self._troca(idx, pai)
      idx = pai
      pai = (idx - 1) // 2

  def _desce(self, idx):
    menor = idx
    esq = 2 * idx + 1
    dir = 2 * idx + 2

    if esq < len(self.data) and self.data[esq] < self.data[menor]:
      menor = esq
    if dir < len(self.data) and self.data[dir] < self.data[menor]:
      menor = dir

    if menor != idx:
      self._troca(idx, menor)
      self._desce(menor)

  def _troca(self, i, j):
    self.data[i], self.data[j] = self.data[j], self.data[i]

  def __len__(self):
    return len(self.data)

  def heapify(self):
    for i in reversed(range(len(self.data) // 2)):
      self._desce(i)

def ler_parametros():
  if len(sys.argv) != 4:
    exit(1)

  p = int(sys.argv[1])
  if p < 2:
    exit(1)

  entrada = sys.argv[2]
  saida = sys.argv[3]
  return p, entrada, saida

def contar_registros(nome_arquivo):
  with open(nome_arquivo, 'r') as f:
    return sum(1 for _ in f)

def criar_runs(nome_entrada, tamanho_heap):
  arquivos_runs = []
  heap = MinHeap()
  buffer = []

  with open(nome_entrada, 'r') as entrada:
    for _ in range(tamanho_heap):
      linha = entrada.readline()
      if not linha:
        break
      heap.push(int(linha.strip()))

    ultimo_escrito = -float('inf')

    while len(heap) > 0:
      run_temp = tempfile.NamedTemporaryFile(delete=False, mode='w')
      arquivos_runs.append(run_temp.name)

      while len(heap) > 0:
        menor = heap.pop()
        run_temp.write(str(menor) + "\n")
        ultimo_escrito = menor

        nova_linha = entrada.readline()
        if not nova_linha:
          continue
        proximo_num = int(nova_linha.strip())

        if proximo_num >= ultimo_escrito:
          heap.push(proximo_num)
        else:
          buffer.append(proximo_num)

      run_temp.close()
      heap = MinHeap()
      for item in buffer:
        heap.push(item)
      buffer = []

  return arquivos_runs

def intercalar_arquivos(runs, p):
  total_passagens = 0

  while len(runs) > 1:
    novos_runs = []
    for i in range(0, len(runs), p):
      grupo = runs[i:i + p]
      temp_out = tempfile.NamedTemporaryFile(delete=False, mode='w')
      intercalar_grupo(grupo, temp_out.name)
      novos_runs.append(temp_out.name)

      for arquivo in grupo:
        os.remove(arquivo)

    runs = novos_runs
    total_passagens += 1

  return runs[0], total_passagens

def intercalar_grupo(arquivos, saida):
  arquivos_abertos = []
  heap = MinHeap()

  for i, nome in enumerate(arquivos):
    f = open(nome, 'r')
    arquivos_abertos.append(f)
    linha = f.readline()
    if linha:
      heap.push((int(linha.strip()), i))

  with open(saida, 'w') as out:
    while len(heap) > 0:
      menor, origem = heap.pop()
      out.write(str(menor) + "\n")
      nova_linha = arquivos_abertos[origem].readline()
      if nova_linha:
        heap.push((int(nova_linha.strip()), origem))

  for f in arquivos_abertos:
    f.close()

def main():
  p, entrada, saida = ler_parametros()
  total = contar_registros(entrada)

  runs = criar_runs(entrada, p)
  num_runs = len(runs)

  resultado_final, num_passes = intercalar_arquivos(runs, p)
  shutil.copy(resultado_final, saida)
  os.remove(resultado_final)

  print("#Regs Ways #Runs #Parses")
  print(f"{total} {p} {num_runs} {num_passes}")

if __name__ == "__main__":
  main()
