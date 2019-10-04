package brush;

import javax.swing.*;
import java.awt.*;

public class MyBrush_ver1 extends JPanel {

    public MyBrush_ver1() {
        setOpaque(true);
    }
    
    @Override
    protected void paintComponent(Graphics g) {

        Graphics2D g2d = (Graphics2D)g;

        super.paintComponent(g);
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        g2d.setColor(Color.blue);
        g2d.fillOval(10, 10, getWidth() - 20, getHeight() * 2 - 20);
        g2d.setColor(Color.red);
        g2d.fillOval(20, 20, getWidth() - 40, getHeight() - 40);
        g2d.setColor(Color.yellow);
        g2d.fillOval(30, 30, getWidth() - 60, getHeight() - 60);
        g2d.setColor(Color.black);
        g2d.fillOval(getWidth()/4 - getWidth()/16, getHeight()/2 - getHeight()/8, getWidth()/8, getHeight()/8);
        g2d.fillOval(getWidth()*3/4 - getWidth()/16, getHeight()/2 - getHeight()/8, getWidth()/8, getHeight()/8);
        g2d.setStroke(new BasicStroke(10, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND));
        g2d.drawArc(getWidth()/4, getHeight()/4, getWidth()/2, getHeight()/2, 225, 90);
    }
}