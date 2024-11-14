/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isValidBST(root: TreeNode | null): boolean {
    const is_valid = (head:TreeNode, min, max):boolean => {
        if(head === null) {
            return true
        } 
        if (head.val > min && head.val < max) {
            const left:boolean = is_valid(head.left, min, head.val);
            const right:boolean = is_valid(head.right, head.val, max)
            return left && right
        } else return false
    } 
    return is_valid(root, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER)
};