class Solution:
    @classmethod
    def buildingOutline(cls, buildings_items):
        print(buildings_items.__len__())
        # 1、取出所有的坐标点
        all_x_points = []
        for building in buildings_items:
            print(buildings_items.index(building))
            if not all_x_points.__contains__(building[0]):
                all_x_points.append(building[0])
            if not all_x_points.__contains__(building[1]):
                all_x_points.append(building[1])

        print("第一步完成")
        # 2、对所有的坐标点从小到大排序
        all_x_points.sort()
        print("第二步完成")
        # 3、根据上述的坐标点划分最小区间
        all_x_tuples = []
        for index in range(1, all_x_points.__len__()):
            all_x_tuples.append((all_x_points[index - 1], all_x_points[index]))
        print("第三步完成")
        # 4、计算每个小最贱区间的最大高度
        all_x_tuple_with_hign = []
        for x_tuple in all_x_tuples:
            x_tuple_with_hign = list(x_tuple)
            x_tuple_with_hign.append(0)
            for building in buildings_items:
                # 最小区间坐落在建筑物内，如果最小区间和建筑物有重合，则一定处于建筑物内。并且赋予最大高度
                if (not x_tuple_with_hign[1] <= building[0]) and (not x_tuple_with_hign[0] >= building[1]) and (
                            building[2] > x_tuple_with_hign[2]):
                    x_tuple_with_hign[2] = building[2]
            if x_tuple_with_hign[2] > 0:
                # 至于高度大于0的区间才是和建筑物重合的区间，否则为无效区间
                all_x_tuple_with_hign.append(x_tuple_with_hign)
        print("第四步完成")
        results = cls.merge_min_building(all_x_tuple_with_hign)
        return results

    @classmethod
    def merge_min_building(cls, building_items, start_index=1):
        """
        合并建筑物区间
        :param building_items: 待合并的建筑物轮廓值
        :param start_index: 开始便利的起点。以免之前比较过的轮廓再次进行多余的比较
        :return: 合并后的建筑物轮廓
        """
        for index in range(start_index, building_items.__len__()):
            if building_items[index-1][2] == building_items[index][2]:
                new_tuple = [building_items[index - 1][0], building_items[index][1], building_items[index][2]]
                return cls.merge_min_building(building_items[0:index - 1] + [new_tuple] + building_items[index + 1:], index)
        return building_items


def test_big_file_text():
    file_object = open('15.in', 'r')
    try:
        all_the_text = file_object.read()
        all_the_text = all_the_text.lstrip('[')
        all_the_text = all_the_text.rstrip("]")
        # all_the_text = all_the_text.replace("'", "")
        all_the_text_list = all_the_text.split("],[")

        buildings = []
        for text_list in all_the_text_list:
            building = text_list.split(",")
            building = [int(x) for x in building]
            buildings.append(building)
        building_outlines = Solution.buildingOutline(buildings)
        print(building_outlines)
    except:
        print("文件读取失败")
    finally:
        file_object.close()

def test_small_text():
    buildings = [[2, 299999, 90], [3, 299998, 37], [4, 299997, 745], [5, 299996, 350], [6, 299995, 969],
                 [7, 299994, 436],
                 [8, 299993, 182], [9, 299992, 327], [10, 299991, 354], [11, 299990, 260], [12, 299989, 165],
                 [13, 299988, 250],
                 [14, 299987, 211], [15, 299986, 462], [16, 299985, 645], [17, 299984, 578], [18, 299983, 422],
                 [19, 299982, 503],
                 [20, 299981, 145], [21, 299980, 723], [22, 299979, 163], [23, 299978, 505], [24, 299977, 246],
                 [25, 299976, 460],
                 [26, 299975, 138], [27, 299974, 691], [28, 299973, 425], [29, 299972, 207], [30, 299971, 114],
                 [31, 299970, 309],
                 [32, 299969, 362], [33, 299968, 425], [34, 299967, 241], [35, 299966, 394], [36, 299965, 931],
                 [37, 299964, 193],
                 [38, 299963, 637], [39, 299962, 920], [40, 299961, 747], [41, 299960, 420], [42, 299959, 950],
                 [43, 299958, 422],
                 [44, 299957, 351], [45, 299956, 423], [46, 299955, 576], [47, 299954, 133], [48, 299953, 312],
                 [49, 299952, 888],
                 [50, 299951, 406], [51, 299950, 113], [52, 299949, 578], [53, 299948, 745], [54, 299947, 758],
                 [55, 299946, 144],
                 [56, 299945, 115], [57, 299944, 694], [58, 299943, 971], [59, 299942, 735], [60, 299941, 519],
                 [61, 299940, 610],
                 [62, 299939, 801], [63, 299938, 850], [64, 299937, 253], [65, 299936, 665]]
    building_outlines = Solution.buildingOutline(buildings)
    print(building_outlines)


if __name__ == '__main__':
    test_big_file_text()
    # test_small_text()