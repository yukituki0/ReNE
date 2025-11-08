# 시각화 데이터 준비
def get_viz_grid(grid, title):
  viz_grid = grid.copy().astype(float)

  # 탐색한 노드 표시
  for v in visited:
      if viz_grid[v] == 0:
          viz_grid[v] = 5

  # 경로 표시
  for p in path:
      viz_grid[p] = 4

  # 시작점, 종료점 표시
  viz_grid[scaled_start_node] = 2
  viz_grid[scaled_end_node] = 3

  # 시각화
  colors = ['white', 'black', 'green', 'red', 'blue', 'lightgray']
  bounds = [0, 1, 2, 3, 4, 5, 6]
  cmap = mcolors.ListedColormap(colors)
  norm = mcolors.BoundaryNorm(bounds, cmap.N)

  plt.figure(figsize=(10, 10))

  plt.imshow(viz_grid, cmap=cmap, norm=norm, interpolation='nearest')

  plt.title(title, fontsize=16)

  # 축 눈금 제거
  plt.xticks([])
  plt.yticks([])

  # 셀 경계선 표시
  ax = plt.gca()
  ax.set_xticks(np.arange(-.5, viz_grid.shape[1], 1), minor=True)
  ax.set_yticks(np.arange(-.5, viz_grid.shape[0], 1), minor=True)
  ax.grid(which="minor", color="gray", linestyle='-', linewidth=0.5)
  ax.tick_params(which="minor", size=0)

  plt.show()
